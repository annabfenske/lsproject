package main

import (
    "fmt"
    "os"
    redis "github.com/garyburd/redigo/redis"
)

func main() {
    cursor, err := redis.DialURL(os.Getenv("REDIS_URL"))
    if err != nil {
        fmt.Println("$$$ could not connect to redis")
    }
    defer cursor.Close()
    fmt.Println("$$$ successfully connected to redis: %s", os.Getenv("REDIS_URL"))
    os.Exit(0)
}
