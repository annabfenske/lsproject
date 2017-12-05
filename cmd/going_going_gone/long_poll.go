package main

import (
    _ "github.com/lib/pq"
    "database/sql"
    "time"
)

func LongPoll(database *sql.DB) {
  for {
        start := time.Now()
        response, error := database.Query()
        elapsed := time.Since(start)

        status := response.StatusCode

        if elapsed.Seconds() >= 30 || error != nil {
            fmt.Println("took longer than 30 seconds")
            fmt.Println(status)

            status := -1
            fmt.Fprintf(file, "%d, %d\n", time.Now().Unix(), status)
        } else {
            fmt.Println("took less than 30 seconds")
            fmt.Println(status)

            fmt.Fprintf(file, "%d, %d\n", time.Now().Unix(), status)

            sleep := (30 * time.Second).Seconds() - elapsed.Seconds()
            time.Sleep(time.Duration(sleep) * time.Second)
        }

        defer response.Body.Close()
    }
}