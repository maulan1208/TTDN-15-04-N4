from odoo import models, fields, api
from datetime import datetime, time

class ChamCong(models.Model):
    _name = 'cham_cong'
    _description = 'Bảng chứa thông tin chấm công'

    nhan_vien_id = fields.Many2one("nhan_su.nhan_vien", string= "Nhân viên", required=True)
    ngay_lam_viec = fields.Date("Ngày làm việc", required = True)
    gio_vao = fields.Datetime(string="Giờ vào")
    gio_ra = fields.Datetime(string="Giờ ra")
    trang_thai = fields.Selection([
        ("Đúng giờ", "Đúng giờ"),
        ("Đi muộn", "Đi muộn"),
        ("Vắng", "Vắng"),
    # ], string="Trạng thái", default = "Vắng")  
    ], string="Trạng thái", compute = "trangThai", store = True)  
    
    @api.depends("gio_vao")
    def trangThai(self):
        for record in self:
            if record.gio_vao and record.ngay_lam_viec:
                gio_vao_d  = datetime.combine(record.ngay_lam_viec, time(8, 0, 0))
                gio_vao_tt = fields.Datetime.to_datetime(record.gio_vao)
                if gio_vao_tt > gio_vao_d :
                    record.trang_thai = "Đi muộn"
                else:
                    record.trang_thai = "Đúng giờ"
            else:
                record.trang_thai = "Vắng"