def capitalize(function):
    def inner(name):
        return function(name.capitalize())

    return inner

def reverse(fn):
    def inner(name):
        return fn(name[::-1])

    return inner


def hello(name):
    return f'Hello {name}'

print(hello('jarosław'))

def (fn):
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        

    return inner


# def gen_html(fn):
#     def inner(name):
#         result = fn(f'<b>{name}</b>')
#         return f'<h1>{result}</h1>'
#
#
#     return inner

def inner_wrapper(fn, tag, highlight, **styles):
    username_styles = "".join(f'{key}: {value}; ' for key, value in styles['username'].items())
    title_styles = "".join(f'{key}: {value}; ' for key, value in styles['title'].items())

    def inner(name):
        result = fn(f'<{highlight} style="{username_styles}">{name}</{highlight}>')
        return f'<{tag} style="{title_styles}">{result}</{tag}>'

    return inner


def gen_html(cb=None, *, tag='h1', highlight = 'b', **styles): # możnaby jeszcze (cb=None, *, tag='h1', highlight='b')

    if callable(cb):
        return inner_wrapper(cb, tag, highlight, **styles)

    def wrapper(cb_):
        return inner_wrapper(cb_, tag, highlight, **styles)

    return wrapper

# Napisz generator stron www, który przyjmie output z funkcji i wstawi go w zasadne miejsce na stronie www

def html_template(template_path, output_path):
    def wrapper(fn):
        def inner(*args, **kwargs):
            result = fn(*args, **kwargs)
            with open(template_path) as template:
                template_text = template.read().replace('{{placeholder}}', result)

            with open(output_path, mode='w') as file:
                file.write(template_text)

            return result
        return inner

    return wrapper


@html_template('template.html', 'hello.html')
@capitalize
@gen_html # lub gen_html() !!
def hello(name):
    return f'Hello {name}'


print(hello('ola')) # <h1>Hello <b>Ola</b></h1>





