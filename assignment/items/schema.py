import graphene
from graphene_django import DjangoObjectType
from .models import Items,CategoryA
from django.db.models import Q

class ItemsType(DjangoObjectType):
    class Meta:
        model = Items

# Query to get data from the server
class Query(graphene.ObjectType):
    items = graphene.List(ItemsType,
                           search=graphene.String(),
                           first=graphene.Int(),
                           skip=graphene.Int(),
                           last=graphene.Int(),
                           )

    def resolve_items(self, info, search=None, first=None, skip=None, last=None, **kwargs):
        qs = Items.objects.all()

        # Search records which partially matches name and url
        if search:
            filter = (
                Q(itemname__icontains=search) |
                Q(cat__icontains=search)
            )
            qs = qs.filter(filter)

        # Skip n records
        if skip:
            qs = qs[skip::]

        # Get the first n records
        if first:
            qs = qs[:first]

        # Get the last n records
        if last:
            last_n = qs.order_by('-id')[:last]
            qs = reversed(last_n)
        return qs
# Create new Items
class CreateItems(graphene.Mutation):
    id = graphene.Int()
    itemname = graphene.String()
    cat = graphene.String()


    class Arguments:
        itemname = graphene.String()
        cat = graphene.String()


    def mutate(self, info, itemname,cat):
        items = Items(itemname=itemname,
                      cat = CategoryA.objects.create(catagery_name=cat),
                      #cat=cat
                      )
        items.save()

        return CreateItems(
            id=items.id,
            itemname=items.itemname,
            cat = items.cat
        )


# Create event to the server
class Mutation(graphene.ObjectType):
    create_item = CreateItems.Field()

