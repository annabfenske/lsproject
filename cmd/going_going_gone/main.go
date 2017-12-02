package main

import (
    "fmt"
    "os"
    redis "github.com/garyburd/redigo/redis"
)

const int ttl = 60 // 60 seconds. Change for production.

func main() {
    cursor, err := redis.DialURL(os.Getenv("REDIS_URL"))
    if err != nil {
        fmt.Println("$$$ could not connect to redis")
        os.Exit(1)
    }
    defer cursor.Close()
    SetID(cursor, "aks516", ttl)

    fmt.Println("$$$ successfully connected to redis: %s", os.Getenv("REDIS_URL"))
    os.Exit(0)
}
