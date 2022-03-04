# md2html
A very common, markdown HTML conversion program.

# Support
Follows Discord markdown notation.  
In time, we will add a mode to support GitHub's notation.

---
## Discord notation
### Headline
```md
# hello!
## Subtitle!
### Subsubtitle!
#### SubSub...SubTitle!
##### Sub(x5)title!
###### SixSubTitle!
```
to
```html
<h1>hello!</h1>
<h2>Subtitle!</h2>
<h3>Subsubtitle!</h3>
<h4>SubSub...SubTitle!</h4>
<h5>Sub(x5)title!</h5>
<h6>SixSubTitle!</h6>
```

### Bold
```md
The **BOLD!!** text!!
```
to
```html
The <b>BOLD!!</b> text!!
```

### Italic
```md
*pasta* is _delicious_ food...
```
to
```html
<i>pasta</i> is <i>delicious</i> food...
```

### Underline
```md
The __important__ text!!
```
to
```html
The <u>important</u> text!!
```

### Strikethrough
```md
The ~~secret~~ message!!
```
to
```html
The <s>secret</s> message!!
```

### Horizontalrule
```md
---
hello!
-----
```
to
```html
<hr>
hello!
<hr>
```

---

# How to use
...(Thinking now...)