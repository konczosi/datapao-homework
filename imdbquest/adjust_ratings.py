def oscar_calculator(oscars_count: int) -> float:
    """Adjust movies ratings based on number of Oscars won"""
    rating_adjustment = 0
    if (oscars_count >= 1) and (oscars_count <= 2):
        rating_adjustment = 0.3
    elif (oscars_count >= 3) and (oscars_count <= 5):
        rating_adjustment = 0.5
    elif (oscars_count >= 6) and (oscars_count <= 10):
        rating_adjustment = 1.0
    elif oscars_count >= 10:
        rating_adjustment = 1.5
    return rating_adjustment

def review_penalizer(review_max: int, review_count: int) -> float:
    """Adjust movie ratings based on number of reviews"""
    rating_adjustment = 0
    review_diff = review_max - review_count
    rating_adjustment = (review_diff // 100_000) * 0.1
    return rating_adjustment
