class Config(object):

    SWAGGER = {
        'title': '너나들이',
        'specs_route': '/api/docs',
        'uiversion': 3,

        'info': {
            'title': '너나들이 API',
            'version': '0.1',
            'description': '너나들이 API 명세서입니다.'
        },
        'host': '52.78.227.70:5001 ',
        'basePath': '/api/',
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ],
        'tags': [
            {
                'name': 'login',
                'description': '로그인/회원가입'
            },
            {
                'name': 'my-page',
                'description': '마이페이지 정보'
            },
            {
                'name': 'posts',
                'description': '게시글'
            },
            {
                'name': 'user',
                'description': '유저'
            }
        ]
    }

    JSON_AS_ASCII = False
