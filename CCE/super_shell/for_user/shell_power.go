package main

import (
	"context"
	"crypto/sha1"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
	"os"
	"os/exec"
	"regexp"
	"strconv"
	"strings"
	"time"
)

type returnObject struct {
	Status  bool   `json:"status"`
	Message string `json:"message"`
	Data    string `json:"Data"`
}

func main() {
	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/uploads", uploadHandler)
	http.HandleFunc("/run", runScriptHandler)

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
		log.Printf("Defaulting to port %s", port)
	}

	log.Printf("Listening on port %s", port)
	log.Printf("Open http://localhost:%s in the browser", port)
	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%s", port), nil))
}


func uploadHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != "POST" {
		returnObjectHandler(w, false, http.StatusText(http.StatusBadRequest), "ERROR")
		return
	}

	body, err := ioutil.ReadAll(r.Body)
	if err != nil {
		returnObjectHandler(w, false, http.StatusText(http.StatusBadRequest), "where is my data")
		return
	}
	defer r.Body.Close()

	if len(body) > 50 { // not sure, file is a big
		returnObjectHandler(w, false, http.StatusText(http.StatusBadRequest), "long long command line-["+string(body)+"]")
		return
	}

	filename := strconv.Itoa(int(time.Now().Unix()))
	filePath := "upload\\" + string(filename) + ".ps1"
	fileErr := ioutil.WriteFile(filePath, []byte(body), 0644)

	if fileErr != nil {
		returnObjectHandler(w, false, http.StatusText(http.StatusBadRequest), "fileErr")
		return
	}
	result := fmt.Sprintf("%x", sha1.Sum([]byte(filename)))
	returnObjectHandler(w, true, http.StatusText(http.StatusOK), "upload\\"+result+".ps1") // hey!! Don't use this function,,
}

func runScriptHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != "GET" {
		returnObjectHandler(w, false, http.StatusText(http.StatusBadRequest), "Not Support Method")
		return
	}

	if r.Method == "GET" {
		if q := r.URL.Query().Get("q"); string(q) != "" && len(q) < 80 {
			// TODO
			// html template
			// ...

			// TODO
			// filtering command keywords
			query, err := url.QueryUnescape(q)
			if err != nil {
				returnObjectHandler(w, false, http.StatusText(http.StatusBadRequest), "queryErr")
				return
			}

			if result, filter := filterObjectHandler(string(query)); !result {
				returnObjectHandler(w, false, http.StatusText(http.StatusBadRequest), "Hey Flag is mine!! don't used ["+filter+"]")
				return
			}

			ctx, cancel := context.WithTimeout(context.Background(), time.Second*3)
			defer cancel()

			// Not really needed some more command lines because PowerShell is super shell.
			commandErr := exec.CommandContext(ctx, "pwsh", "-Command", string(query)).Run()
			ctx.Done()

			// No Hack my Super Shell!
			if commandErr != nil {
				returnObjectHandler(w, false, http.StatusText(http.StatusBadRequest), "No Hack")
				return
			}

			returnObjectHandler(w, true, http.StatusText(http.StatusOK), "Success")
			return
		} else {
			returnObjectHandler(w, false, http.StatusText(http.StatusBadRequest), "queryErr")
			return
		}
	}
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		http.NotFound(w, r)
		return
	}

	_, err := fmt.Fprint(w, "Do You Have a Super Shell? I Have Super Shell!")
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}
}

func filterObjectHandler(target string) (bool, string) {
	// Not sure,, but You can use another command. I think that lol
	// Oh! There's a hint I forgot to tell you! None of the values in the flag match the string being filtered!
	regexPattern := "(?i)(flag|win|http|net|cert|ac|asnp|cat|cd|CFS|chdir|clc|clear|clhy|cli|clp|cls|clv|cnsn|compare|copy|cp|cpi|cpp|curl|cvpa|dbp|del|diff|dir|dnsn|ebp|echo|epal|epcsv|epsn|erase|etsn|exsn|fc|fhx|fl|foreach|ft|fw|gbp|gc|gcb|gci|gcm|gcs|gdr|ghy|gi|gin|gjb|gl|gm|gmo|gp|gps|gpvue|group|gsn|gsnp|gsv|gtz|gu|gv|gwmi|h|history|icm|iex|ihy|ii|ipal|ipcsv|ipmo|ipsn|irm|ise|iwmi|iwr|kill|lp|ls|md|measure|mi|mount|move|mp|mv|nal|ndr|ni|nmo|npsscurationFile|nsn|nv|ogv|oh|popd|ps|pushd|pwd|rbp|rcjb|rcsn|rd|rdr|ren|ri|rjb|rm|rm|timeout|fdir|rmo|rni|rnp|rp|rsn|rsnp|rujb|rv|rvpa|rwmi|sajb|sal|saps|sasv|sbp|sc|scb|select|set|shcm|si|sls|sort|sp|spjb|spps|spsv|start|stz|sujb|sv|swmi|tee|trcm|wget|where|wjb|write|more|find|uname|date|cut|file|ssh|nc|fc|exit|tail|less|wc|tar|zip|lib|ping|add|su|df|cal)"
	regex := regexp.MustCompile(regexPattern)
	matchingPattern := regex.FindAllString(target, -1)

	if matchingPattern != nil || len(matchingPattern) != 0 {
		var result string
		for i, v := range matchingPattern {
			if i > 0 {
				result += ", "
			}
			result += v
		}
		return false, result
	}

	var contains = []string{
		"`", "-", ",", "\\", "\"", "_", "~", "!", ">", "<", "=", "+", "%", "?", ".", "[", "]", "&", ";", "@", "/", "$",
	}

	for _, filter := range contains {
		if strings.Contains(target, filter) {
			return false, filter
		}
	}
	return true, ""
}

func returnObjectHandler(w http.ResponseWriter, status bool, message string, data string) {
	response := returnObject{
		Status:  status,
		Message: message,
		Data:    data,
	}

	jsonResponse, err := json.Marshal(response)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write(jsonResponse)
}
