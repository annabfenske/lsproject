package main

import (
    redis "github.com/garyburd/redigo/redis"
    "fmt"
)

func SetID(connection redis.Conn, id string, ttl float64) {
    idkey := ":1:" + id
    reply, err := connection.Do("SETEX", idkey, ttl, 1)
    if err != nil {
        fmt.Println(err)
    }
}

func SetIDs(connection redis.Conn, ids []string, ttl float64) {
    for _, id := range ids {
        SetID(connection, id, ttl)
    }
}
