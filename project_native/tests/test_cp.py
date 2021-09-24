from odoo.tests.common import TransactionCase
from odoo.tests import common
from datetime import datetime, timedelta


class TestProject(common.TransactionCase):

    def test_create_data(self):
        # Create a new project with the test
        test_project = self.env['project.project'].create({
            'name': 'TestProject'
        })

        # Add a test task to the project
        test_project_task = self.env['project.task'].create({
            'name': 'ExampleTask',
            'project_id': test_project.id
        })

        # Check if the project name and the task name match
        self.assertEqual(test_project.name, 'TestProject')
        self.assertEqual(test_project_task.name, 'ExampleTask')
        # Check if the project assigned to the task is in fact the correct id
        self.assertEqual(test_project_task.project_id.id, test_project.id)
        # Do a little print to show it visually for this demo - in production you don't really need this.
        print('Your test was succesfull!')

    # def test_check_load_factor(self):
    #     # Create a new project with the test
    #     test_task = self.env['project.task']
    #
    #     _load_factor = 0.5
    #     hour_from = timedelta(hours=8)
    #     hour_to = timedelta(hours=12)
    #     len_attendances = 2
    #     inx = 1
    #     work_att = timedelta(hours=4)

        # def check_load_factor(self, _load_factor, hour_to, hour_from, len_attendances, inx, work_att):

        # # Add a test task to the project
        # test_project_task = self.env['project.task'].create({
        #     'name': 'ExampleTask',
        #     'project_id': test_project.id
        # })
        #
        # # Check if the project name and the task name match
        # self.assertEqual(test_project.name, 'TestProject')
        # self.assertEqual(test_project_task.name, 'ExampleTask')
        # # Check if the project assigned to the task is in fact the correct id
        # self.assertEqual(test_project_task.project_id.id, test_project.id)
        # # Do a little print to show it visually for this demo - in production you don't really need this.
        # print('Your test was succesfull!')