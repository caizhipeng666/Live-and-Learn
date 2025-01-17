# JWT
> Json Web Token   
---
### JWT与其他登录认证的区别
1. Session
   在session中保存相关数据，如用户角色、登录时间等,   
   此后，用户的每一次请求，都会通过Cookie，将session_id传回服务器   
   ❌但Session扩展性差   
      体现在跨域上，session在单点上没有问题，但在集群和跨域上   
2. 写入数据库   
   (1)工程量大，速度无法保证   
   (2)如果数据库挂了，单点都无法通过   
3. JWT   
   服务器认证以后，生成一个JSON对象，返回给用户   
   以后，用户与服务器通信的时候，都要发送这个JSON对象   
   (1)服务器变成无状态，不保存任何session数据   
   (2)不仅可以用于认证，也可以用于交换信息，有效的使用可以减少数据库交互   
   (3)缺点:一旦签发了JWT，在到期之前无法失效   
   (4)缺点:×一旦泄露，任何人都可以获得该令牌的所有权限   
   (5)缺点:默认不加密，但可以在生成原始token后再使用密钥加密一次   
---
### JWT结构
1. 消息头 header(通过BASE64URL)
   > 描述JWT元数据
```
{
  "alg":"HS256(算法)"
  "typ":"JWT(类型)"
}
```
2. 消息体 payload(通过BASE64URL)
```
官方选用字段
iss:签发人
exp:过期时间
sub:主题
aud:受众
nbf:生效时间
iat:签发时间
jti:编号

也可以自定义私有字段
...
```
3. 签名 signature(HMACSHA256)
```
通过服务器密钥，使用Header里指定的签名算法(alg)产生签名
```
---
### JWT使用方法
客户端收到的JWT:
   1. 存放在Cookie，使用HttpOnly=True(防御xss)
   2. 存放在localStorage   
   ▲容易受到xss跨域脚本攻击

客户端与服务器交互:
   1. 每次通信都带上JWT
   2. 可以放在Cookie中自动发送，但无法跨域
   3. ✔最好的做法就是放在HTTP请求头的Authorization里面
