import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data

# Set a custom color cycle for Matplotlib charts
plt.rcParams['axes.prop_cycle'] = plt.cycler(
    color=['#4C2A85', '#BE96FF', '#957DAD', '5E366E', '#A98CCC']
)

# Chart 1: Sales by Product
fig1 = Figure(figsize=(4, 4))
ax1 = fig1.add_subplot(111)
ax1.bar(sales_data.keys(), sales_data.values())
ax1.set_title('Sales by Product')
ax1.set_xlabel('Product')  # Fix: Use parentheses to set xlabel
ax1.set_ylabel('Sales')    # Fix: Use parentheses to set ylabel
# plt.show()

# Chart 2: Inventory by Product
fig2 = Figure(figsize=(4, 4))
ax2 = fig2.add_subplot(111)
ax2.barh(list(inventory_data.keys()), inventory_data.values())
ax2.set_title('Inventory by Product')
ax2.set_xlabel('Inventory')
ax2.set_ylabel('Product')
# plt.show()

# Chart 3: Product Breakdown
fig3 = Figure(figsize=(4, 4))
ax3 = fig3.add_subplot(111)
ax3.pie(product_data.values(), labels=product_data.keys(),
        colors=['red', 'green', 'blue', 'yellow'], autopct='%1.1f%%')
ax3.set_title('Product Breakdown')
# plt.show()

# Chart 4: Sales by Years
fig4 = Figure(figsize=(4, 4))
ax4 = fig4.add_subplot(111)
ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
ax4.set_title('Sales by Years')
ax4.set_xlabel('Year')
ax4.set_ylabel('Sales')
# plt.show()

# Chart 5: Inventory by Month
fig5 = Figure(figsize=(4, 4))
ax5 = fig5.add_subplot(111)
ax5.fill_between(inventory_month_data.keys(), inventory_month_data.values())
ax5.set_title('Inventory by Month')
ax5.set_xlabel('Month')
ax5.set_ylabel('Inventory')
# plt.show()

# Create the Tkinter window and layout
window = tk.Tk()
window.title('Dashboard')
window.state('zoomed')
side_frame = tk.Frame(window, bg='#4C2A85')
side_frame.pack(side='left', fill='y')
label = tk.Label(side_frame, text='Dashboard',
                 bg='#4C2A85', fg='#FFF', font=25)
label.pack(pady=50, padx=20)
charts_frame = tk.Frame(window)
charts_frame.pack()
upper_frame = tk.Frame(charts_frame)
upper_frame.grid(row=0, column=0)
canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().grid(row=0, column=0, sticky='nsew')
canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().grid(row=0, column=1, sticky='nsew')
canvas3 = FigureCanvasTkAgg(fig3, upper_frame)
canvas3.draw()
canvas3.get_tk_widget().grid(row=0, column=2, sticky='nsew')

lower_frame = tk.Frame(charts_frame)
lower_frame.grid(row=1, column=0)
canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
canvas4.draw()
canvas4.get_tk_widget().grid(row=0, column=0, sticky='nsew')
canvas5 = FigureCanvasTkAgg(fig5, lower_frame)
canvas5.draw()
canvas5.get_tk_widget().grid(row=0, column=1, sticky='nsew')

# Start the Tkinter event loop
window.mainloop()
