from environs import Env

env = Env()
env.read_env()

is_debug = env.bool('DEBUG', default=False)

token = env('API_TOKEN')

developer_id = env('DEVELOPER_ID')
