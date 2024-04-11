from environs import Env


env = Env()
env.read_env()

main_bot = env.str("main_bot")

bd_host = env.str("bd_host")
bd_login = env.str("bd_login")
bd_pass = env.str("bd_pass")
bd_base = env.str("bd_base")

admin_id = 1806031898
