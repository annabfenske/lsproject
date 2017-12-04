package main

import (
    "fmt"
    "os"
    redis "github.com/garyburd/redigo/redis"
    _ "github.com/lib/pq"
    "database/sql"
)

const ttl = 60 // 60 seconds. Change for production.

func main() {
    rConn, err := redis.DialURL(os.Getenv("REDIS_URL"))
    if err != nil {
        fmt.Println("$$$ could not connect to redis")
        os.Exit(1)
    }
    SetIDs(rConn, []string{"aks516", "idk152", "whodis", "newphone"}, ttl)
    defer rConn.Close()
    fmt.Println("$$$ successfully connected to redis:", os.Getenv("REDIS_URL"))

    postgres, err := sql.Open("postgres", os.Getenv("DATABASE_URL"))
    if err != nil {
        fmt.Println("$$$ could not connect to postgres")
        os.Exit(1)
    }
    defer postgres.Close()
    fmt.Println("$$$ successfully connected to postgres:", os.Getenv("DATABASE_URL"))

    os.Exit(0)
}
