import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """
    a, b: 1-D vectors of equal length.

    Returns:
        the cosine of the angle between a and b, or 0.0 if either has
        zero length.
    """
    if(np.linalg.norm(a)==0 or np.linalg.norm(b)==0):
        return 0.0
    ans = np.dot(a,b) / (np.linalg.norm(a)*np.linalg.norm(b))
    return ans
    # TODO: Dot product divided by the product of the norms.
    pass
