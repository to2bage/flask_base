"""
  *@ClassName entry
  *@Description TODO
  *@Author to2bage
  *@Date 2020-07-25 18:10
  *@Version 1.0
 """


from app.app import create_app

app = create_app()


if __name__ == '__main__':
    app.run()