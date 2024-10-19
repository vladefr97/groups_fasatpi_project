from app.domain.entities import Group
from app.persistance.base import BaseGroupPersistence

groups = {
    '1': {
        'id': 1,
        'name': 'first_group',
        'number': '0001'

    },
    '2': {
        'id': 2,
        'name': 'second_group',
        'number': '0002'
    }
}


class GroupDictionaryPersistence(BaseGroupPersistence):
    def get_by_id(self, group_id: int) -> Group | None:
        if f'{group_id}' in groups.keys():
            group_dict = groups[f'{group_id}']
            group = Group(id=group_dict['id'], name=group_dict['name'],
                          number=group_dict['number'])
            return group
        else:
            return None

    def create_group(self, group: Group) -> None:
        groups[f'{group.id}'] = {
            'id': group.id,
            'name': group.name,
            'number': group.number
        }