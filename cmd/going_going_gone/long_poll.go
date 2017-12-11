package main

import (
    "os"
    "fmt"
    "time"
    _ "github.com/lib/pq"
    "database/sql"
)

const pollInterval = 10

func GetIDs(database *sql.DB, tableName string, timeLost string) (*sql.Rows, error) {
  rows, error := database.Query("SELECT net_id FROM  WHERE time_lost>$1", timeLost)
  if error != nil {
      fmt.Println("$$$ could not select rows")
      fmt.Println(error)
      os.Exit(1)
  } 
  return rows, error
}

func LongPoll(database *sql.DB, handler func(string), preset func()) {
    lastCheck := time.Now()
    for {
        queryStart := lastCheck.Add(time.Duration((-pollInterval * time.Second).Seconds()))
        timeLost := queryStart.Format("2006-01-02 15:04:05-07")
        lastCheck = time.Now()
        rows, error := GetIDs(database, "lostandfound_lostnyuid", timeLost)

        preset()
        for rows.Next() {
          var id string
          err := rows.Scan(&id)
          if err != nil {
            fmt.Println("$$$ could not scan rows")
          } else {
            fmt.Println(id)
            handler(id)
          }
        }

        rows.Close()

        elapsed := time.Since(lastCheck)

        if elapsed.Seconds() >= pollInterval || error != nil {
            fmt.Println("took longer than our interval")
        } else {
            fmt.Println("took less than our interval")

            sleep := (pollInterval * time.Second).Seconds() - elapsed.Seconds()
            time.Sleep(time.Duration(sleep) * time.Second)
        }
    }
}