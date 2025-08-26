using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using Accord.MachineLearning;
/*using Accord.Statistics.Filters;*/

namespace _4._1.Áp_dụng_model_vào_thiết_kế_giao_diện
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private DataTable LoadCSV(string file)
        {
            DataTable dt = new DataTable();
            
            try
            {
                using (StreamReader reader=new StreamReader(file))
                {
                    string[] headers = reader.ReadLine().Split(','); // Đọc tiêu đề cột
                    foreach (string header in headers)
                    {
                        dt.Columns.Add(header);
                    }

                    while (!reader.EndOfStream)
                    {
                        string[] rows = reader.ReadLine().Split(',');
                        dt.Rows.Add(rows);
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error loading CSV: " + ex.Message);
            }
            return dt;
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            string File = "D:\\Data Mining\\Size.csv";

            if (string.IsNullOrEmpty(File))
            {
                MessageBox.Show("Please select a file first.");
                return;
            }

            DataTable data = LoadCSV(File); // Đọc dữ liệu
            dataGridView1.DataSource = data; // Hiển thị trên DataGridView
        }

    
        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
