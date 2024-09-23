import tkinter as tk
from login_frames import LoginFrame
from teacher_dashboard import TeacherDashboard
from admin_dashboard import AdminDashboard
from supervisor_dashboard import SupervisorDashboard
from manage_user_frame import ManageUsersFrame
from add_user_frame import AddUserFrame
from teacher_discipline_list_frame import MySubjectsFrame
from teacher_list_frame import TeacherListFrame
from teacher_info_frame import TeacherInfoFrame
from add_teacher_frame import AddTeacherFrame
from discipline_list_frame import DisciplineListFrame
from edit_discioline_frame import EditDisciplineFrame
from group_members_frame import GroupMembersFrame
from group_list_frame import GroupListFrame



class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Educational Management System")
        #self.iconbitmap(default="./SFULogo.ico")
        self.geometry("600x400")
        self.current_frame = None
        self.show_login()
    

    def show_admin_dashboard(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = AdminDashboard(self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_user_list(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = ManageUsersFrame(self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)


    def show_add_user(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = AddUserFrame(self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_supervisor_dashboard(self):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = SupervisorDashboard(self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)


    def show_manage_users(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = ManageUsersFrame(self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_login(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = LoginFrame(self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_teacher_dashboard(self, teacher_id):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = TeacherDashboard(self, teacher_id)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_my_subjects_frame(self, teacher_id):
            if self.current_frame:
                self.current_frame.pack_forget()
            self.current_frame = MySubjectsFrame(self, teacher_id)
            self.current_frame.pack(fill="both", expand=True)
        
    def show_group_members(self, subject_details, teacher_id):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = GroupMembersFrame(self, subject_details, teacher_id)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_teacher_list(self):
        self.current_frame.pack_forget()
        self.current_frame = TeacherListFrame(self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_add_teacher(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = AddTeacherFrame(self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_teacher_info(self, teacher):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = TeacherInfoFrame(self, teacher)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_discipline_list(self, teacher_id):
        self.current_frame.pack_forget()
        self.current_frame = DisciplineListFrame(self, teacher_id)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_edit_discipline(self, discipline, teacher_id):
        if self.current_frame: 
            self.current_frame.destroy()
        self.current_frame = EditDisciplineFrame(self, discipline, teacher_id)
        self.current_frame.pack()

    def show_group_list(self, subject_details, teacher_id):
        self.current_frame.pack_forget()
        self.current_frame = GroupListFrame(self, subject_details, teacher_id)  # Исправлено создание экземпляра GroupListFrame
        self.current_frame.pack(fill=tk.BOTH, expand=True)