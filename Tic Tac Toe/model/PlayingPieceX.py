
from model.PieceType import PieceType
from model.PlayingPiece import PlayingPiece

class PlayingPieceX(PlayingPiece):
    
    def __init__(self):
        super().__init__(PieceType.X)