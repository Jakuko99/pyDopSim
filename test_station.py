import game.api_package as game

if __name__ == "__main__":
    app = game.StationTest()
    app.add_test_bindings()

    app.run()