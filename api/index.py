from app import app

# Vercel需要这个文件作为WSGI入口点
if __name__ == '__main__':
    app.run()
