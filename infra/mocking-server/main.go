package main

import (
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"github.com/go-faker/faker/v4"
)

type Data struct{
	Title 	string `faker:"word"`
	Author	string `faker:"name"`	
	Url 	string `faker:"url,unique"`
	Date	string `faker:"date"`
}

func main() {
	router := gin.Default()
	
	router.GET("/fake-data/:count", getFakeData)
	
	router.Run("0.0.0.0:9000")
}

func getFakeData(c *gin.Context){
	cnt, err := strconv.Atoi(c.Param("count"))
	if err != nil || cnt <= 0 {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"error":"Count must be integer, > 0"})
		return
	}
	
	dataList := make([]Data, 0, cnt)
	
	for i:= 0; i < cnt; i++{
		data := Data{}
		if err := faker.FakeData(&data); err != nil{
			c.IndentedJSON(http.StatusInternalServerError, gin.H{"message": "Fail to create fake data"})
			return
		}
		dataList = append(dataList, data)

	}
	c.IndentedJSON(http.StatusOK, dataList)
}