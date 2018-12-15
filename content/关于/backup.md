---
title: backup
date: 2017-10-09 11:30
status: draft
---

```
---
title: 文档标题
date: <%

function full(string) {
    string = String(string);
    if (string.length == 1) {
        return '0' + string;
    }
    else {
        return string;
    }
}

function time() {
    let date = new Date();
    let year = date.getFullYear();
    let month = full(date.getMonth() + 1);
    let day = full(date.getDate());
    let hour = full(date.getHours());
    let minute = full(date.getMinutes());
    return `${year}-${month}-${day} ${hour}:${minute}`;
}

print(time());

 %>
summary: 
status: draft
---

文档正文
```

