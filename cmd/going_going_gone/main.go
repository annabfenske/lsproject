package main

import (
    "fmt"
    "os"
    redis "github.com/garyburd/redigo/redis"
    _ "github.com/lib/pq"
    "database/sql"
)

const ttl = 30 // 30 seconds. Change for production.

func getWriter(rConn *redis.Conn, ttl float64) func(id string) {
    return func(id string) {
        SetID(rConn, id, ttl)
    }
}

func getRefreshConnection(rConn *redis.Conn) func() {
    return func() {
        if rConn != nil {
            _, err := (*rConn).Do("SET", "CHECK")
            if err != nil {
                *rConn, err = redis.DialURL(os.Getenv("REDIS_URL"))
            }
        } else {
            connection, err := redis.DialURL(os.Getenv("REDIS_URL"))
            if err != nil {
                fmt.Println("$$$ could not connect to redis")
                fmt.Println(err)
                os.Exit(1)
            }
            *rConn = connection
        }
    }
}

func main() {
    connection, err := redis.DialURL(os.Getenv("REDIS_URL"))
    rConn := &connection
    if err != nil {
        fmt.Println("$$$ could not connect to redis")
        os.Exit(1)
    }
    defer (*rConn).Close()
    fmt.Println("$$$ successfully connected to redis:", os.Getenv("REDIS_URL"))

    postgres, err := sql.Open("postgres", os.Getenv("DATABASE_URL"))
    if err != nil {
        fmt.Println("$$$ could not connect to postgres")
        os.Exit(1)
    }
    defer postgres.Close()
    fmt.Println("$$$ successfully connected to postgres:", os.Getenv("DATABASE_URL"))

    handler := getWriter(rConn, ttl)
    refreshConnection := getRefreshConnection(rConn)

    LongPoll(postgres, handler, refreshConnection)

    os.Exit(0)
}
