from flask_restx import reqparse

pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('page', type=int, required=False, default=1, help='Page number')
pagination_arguments.add_argument('per_page', type=int, required=False,
                                  default=2, help='Results per page }')

search_arguments = reqparse.RequestParser()
search_arguments.add_argument('q', type=str, required=True, default="", help='Search query')
