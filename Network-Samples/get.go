package main
/*https://stackoverflow.com/questions/13263492/set-useragent-in-http-request/13263993#13263993
User agent^
*/
import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func returnVal(x int, y int) int {
	autoVar := y * x
	var z int = 56
	fmt.Println("We are now implicitly declaring a type, outputting variable Z:", z)
	return autoVar
}

func changeuserAgent() {
	client := &http.Client{}

	req, err := http.NewRequest("GET", "http://127.0.0.1", nil)
	if err != nil {
		log.Fatalln(err)
	}

	req.Header.Set("User-Agent", "SET THIS")
	//Do == Calling the actual request
	resp, err := client.Do(req) //This actually calls the request
	if err != nil {
		log.Fatalln(err)
	}

	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}
	log.Println(string(body)) //Print the output
}

func main() {
	changeuserAgent()
	test := returnVal(5,6)
	fmt.Println("Printing 6 * 5:", test)
	fmt.Println("Function Call:\n ", test)
}