#  Video Project

# How do i Running project
`
> sudo docker-compose up --build
`

# How do i Make Database
`
> sudo docker-compose run web python3 api/manage.py makemigrations
> sudo docker-compose run web python3 api/manage.py migrate
`

# How do i Remove project
`
> sudo docker-compose down
`

# Sources

## Back End -> Python, Django, DjangoRestFramework
- https://docs.python.org/3/
- https://docs.djangoproject.com/en/2.1/
- https://www.django-rest-framework.org/

## container -> Docker
- https://docs.docker.com/compose/django/


## Front End -> Node, Webpack, Eslint, Bable, Expressjs, Axios -> SPA = Single Page Application
- https://app.pluralsight.com/library/courses/vue-js-single-page-applications/table-of-contents
- https://nodejs.org/api/index.html
- https://expressjs.com/en/starter/installing.html
- https://webpack.js.org/concepts/
- https://vuejs.org/v2/guide/
- https://eslint.org/docs/developer-guide/working-with-rules
- https://vue-loader.vuejs.org/guide/#vue-cli
- https://babeljs.io/docs/en/
