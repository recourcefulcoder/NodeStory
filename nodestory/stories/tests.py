from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import ClosureTable, StoryNode


# def compare_list_and_queryset_without_order(object_list, QuerySet):
#     for object in object_list:
#         found = False
#         for object_query in QuerySet:
#             if object.ancestor_id == object_query.ancestor_id \
#                     and object.descendant_id == object_query.descendant_id \
#                     and object.depth == object_query.depth:
#                 found = True
#         if not found:
#             return False
#     if len(object_list) != len(QuerySet):
#         print(f"LEN: {len(object_list)}, {len(QuerySet)}")
#         return False
#     return True


class StoryNodeModelTesting(TestCase):
    fixtures = ["fixture.json"]

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.user = get_user_model().objects.get(pk=1)
        cls.story1 = StoryNode.objects.create(
            ancestor_id=1,
            author=cls.user,
            text="default text"
        )
        cls.story2 = StoryNode.objects.create(
            ancestor_id=cls.story1.pk,
            author=cls.user,
            text="default continuing text",
        )

    def test_proper_closure_table_row_amount_created(self):
        records1 = ClosureTable.objects.filter(descendant_id=self.story1.id)
        records2 = ClosureTable.objects.filter(descendant_id=self.story2.id)
        self.assertTrue(len(records1) == 2)
        self.assertTrue(len(records2) == 3)

    # def test_correct_closure_table_rows(self):
    #     records1 = ClosureTable.objects.filter(descendant_id=self.story1.id)
    #     records2 = ClosureTable.objects.filter(descendant_id=self.story2.id)
    #     record1 = ClosureTable.objects.filter(
    #         ancestor_id=1,
    #         descendant_id=self.story1.id,
    #         depth=1
    #     )
    #     record2 = ClosureTable(
    #         ancestor_id=self.story1.id,
    #         descendant_id=self.story1.id,
    #         depth=0
    #     )
    #     target_records1 = [record1, record2]
    #     self.assertTrue(
    #         compare_list_and_queryset_without_order(
    #             target_records1, records1
    #         )
    #     )
    #     # self.assertTrue(len(records2) == 3)
