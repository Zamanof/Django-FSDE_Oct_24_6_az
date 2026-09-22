def paginate(
        query,
        page = 1,
        size = 10):
    total = query.count()
    items = query.offset(page - 1).limit(size).all()
    return {
        "count": total,
        "page": page,
        "size": size,
        "results": items
    }
