# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]
# tuple creation
shelf1_update_tuple = tuple(shelf1_update)
# concat
shelf1_concat = shelf1 + shelf1_update_tuple
# Celery index
celery_index = shelf1_concat.index("celery")
# celery count
celery_count = shelf1_concat.count("celery")
#output
print("Updated Shelf #1:",shelf1_concat)
print("celery",":","Number of Celery:",celery_count)
print("celery",":","Celery Index:",celery_index)