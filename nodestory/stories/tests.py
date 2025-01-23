from django.contrib.auth import get_user_model
from django.test import TestCase

from parameterized import parameterized

from .models import ClosureTable, StoryNode


def records_equal(record1, record2):
    return (
        record1.ancestor == record2.ancestor
        and record1.descendant == record2.descendant
        and record1.depth == record2.depth
    )


def unordered_querysets_equal(queryset, object_list, equal_func):
    for object1 in object_list:
        found = False
        for object_query in queryset:
            if equal_func(object_query, object1):
                found = True
        if not found:
            return False
    if len(object_list) != len(queryset):
        return False
    return True


class StoryNodeModelTesting(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.user = get_user_model().objects.create(
            username="default",
            password="default",
        )
        cls.story1 = StoryNode.objects.create(
            author=cls.user, text="default text"
        )
        cls.story2 = StoryNode.objects.create(
            ancestor=cls.story1,
            author=cls.user,
            text="default continuing text",
        )
        cls.story3 = StoryNode.objects.create(
            ancestor=cls.story2,
            author=cls.user,
            text="default continuing text: part2",
        )
        cls.record1 = ClosureTable(
            ancestor=cls.story1, descendant=cls.story1, depth=0
        )
        cls.record2 = ClosureTable(
            ancestor=cls.story1, descendant=cls.story2, depth=1
        )
        cls.record3 = ClosureTable(
            ancestor=cls.story1, descendant=cls.story3, depth=2
        )
        cls.record4 = ClosureTable(
            ancestor=cls.story2, descendant=cls.story3, depth=1
        )

    @parameterized.expand(
        [
            ("story1", 1),
            ("story2", 1),
            ("story3", 2),
        ]
    )
    def test_proper_closure_table_row_amount_created(
        self, story_name, target_amo
    ):
        records = ClosureTable.objects.filter(
            descendant=getattr(self, story_name, None)
        )
        self.assertEqual(len(records), target_amo)

    @parameterized.expand(
        [
            ("story1", ["record1"]),
            ("story2", ["record2"]),
            ("story3", ["record3", "record4"]),
        ]
    )
    def test_correct_closure_table_row(self, story_name, target_names):
        records = ClosureTable.objects.filter(
            descendant=getattr(self, story_name, None)
        )
        target_collection = list()

        for name in target_names:
            target_collection.append(getattr(self, name, None))

        self.assertTrue(
            unordered_querysets_equal(
                records, target_collection, records_equal
            )
        )
        # didn't use assertQuerySetEqual here because for unordered comparison
        # records collection must be transformed into set(), which is
        # impossible because requires hashing, which is
        # not applicable to no-primary-key objects, which are my records.
