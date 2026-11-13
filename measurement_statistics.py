def calculate_statistics(values: list[float]) -> dict:
    if not values:
        raise ValueError("Die Liste darf nicht leer sein.")

    return {
        "count": len(values),
        "mean": sum(values) / len(values),
        "minimum": min(values),
        "maximum": max(values)
    }

if __name__ == "__main__":

    measurements = [19.98, 20.01, 20.03, 19.99, 20.02]

    result = calculate_statistics(measurements)

    print(f"count: {result["count"]}")
    print(f"mean: {result["mean"]:.3f} mm")
    print(f"minimum: {result["minimum"]:.3f} mm")
    print(f"maximum: {result["maximum"]:.3f} mm")
