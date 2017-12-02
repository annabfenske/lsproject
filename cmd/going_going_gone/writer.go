package main

import (
    redis "github.com/garyburd/redigo/redis"
)

func SetID(connection redis.Conn, id string, ttl float64) {
    idkey := ":1:" + id
    connection.Do("SETEX", idkey, ttl, 1)
}
