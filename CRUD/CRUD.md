# API 명세서
(a) path parameter.ver  
(b) query parameter.ver  

### Create - 사용자 생성
(a) POST /users/name/{name}/nickname/{nickname}    
(b) POST /users?name=hello&nickname=world  
```
{
    "status": "success"
}
```  
<br>

### Read - 이름을 입력하여 해당 이름을 가진 별명을 반환
(a) GET /users/name/{name}    
(b) GET /users?name=hello    
``` 
{  
    "nickname": "world"  
}  
```  
<br>

### Update - 이름과 새로운 별명을 입력하여 해당 이름에 대한 정보를 업데이트  
(a) PUT /users/name/{name}/nickname/{nickname}   
(b) PUT /users?name=hello&nickname=world2   
```
{
    "status": "success"
}
```  
<br>

### Delete - 이름을 입력하여 해당 정보를 삭제
(a) DELETE /users/name/{name}   
(b) DELETE /users?name=hello    
```
{
    "status": "success"
}
```