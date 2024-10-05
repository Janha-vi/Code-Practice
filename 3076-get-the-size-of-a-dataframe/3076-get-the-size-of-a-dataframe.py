import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    ans = []
    ans.append(players.shape[0])
    ans.append(players.shape[1])
    return ans
