package main

import (
    "fmt"
    "os"
    redis "github.com/garyburd/redigo/redis"
)

const ttl = 60 // 60 seconds. Change for production.

func main() {
    cursor, err := redis.DialURL(os.Getenv("REDIS_URL"))
    if err != nil {
        fmt.Println("$$$ could not connect to redis")
        os.Exit(1)
    }
    defer cursor.Close()
    SetIDs(cursor, []string{"aks516", "idk152", "whodis", "newphone"}, ttl)

    fmt.Println("$$$ successfully connected to redis: %s", os.Getenv("REDIS_URL"))
    os.Exit(0)
}
