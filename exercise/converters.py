def convert_to_meters(feet, inches):
    """Convert feet and inches to meters."""
    total_inches = feet * 12 + inches
    meters = total_inches * 0.0254
    return meters