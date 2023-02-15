from src.util.loader import loader

class AssetManager:
    def __init__(self):
        self.assets = {
            "login_background": loader.loadImage("res/game_background.jpg"),
            "grass": loader.loadImage("res/tiles/grass1.png"),
            "grassalt": loader.loadImage("res/tiles/grass2.png"),
            "concrete": loader.loadImage("res/tiles/concrete1.png"),
            "concretealt": loader.loadImage("res/tiles/concrete2.png"),
            "dirt": loader.loadImage("res/tiles/dirt.png"),
            "dirstand": loader.loadImage("res/tiles/dirtsand.png"),
            "brick": loader.loadImage("res/tiles/brick.png"),
            "rock": loader.loadImage("res/tiles/rock.png"),
            "snow": loader.loadImage("res/tiles/snow.png"),
            "stone": loader.loadImage("res/tiles/stone.png"),
            "player": loader.loadImage("res/tiles/snow.png")
        }

    def getAsset(self, assetName):
        return self.assets[assetName]

assetManager = AssetManager()