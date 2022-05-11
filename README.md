# htmlobj

An package to create HTML objects from Python.

I build this project to parctice packaging Python projects. Currently only few functions are implemented. Probably I will add more in the future.

## Installation

```bash
pip install -i https://test.pypi.org/simple/ html-jingfelix
```

## Example

```python
import htmlobj

# build an html object
body = htmlobj.HtmlDom('body')
a = htmlobj.HtmlDomA(href='http://www.google.com')

# add a child element to the body
body.addChild(a)

# set class, id and content
body._class = 'main-body'
body._id = 'main-body'
body._content = 'Hello world!'

# print html object
print(body)
# or
print(body.toString())
```

You can also view a complete demo via [this repo](https://github.com/jingfelix/jingfelix.github.io), which uses htmlobj to create part of a simple html page.

## License

```htmlobj``` uses the MIT license.
