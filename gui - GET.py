import tkinter as tk  # tkinter import kiya - GUI toolkit ke liye
from tkinter import ttk, messagebox  # ttk (themed widgets) aur messagebox import kiya

# ============================================================
# LINEAR SOLVER GUI CLASS
# Tkinter se banaya gaya visual interface
# User ko GUI dete hain matrix input aur solution ke liye
# No need for command line - click buttons aur fill boxes
# ============================================================
class LinearSolverGUI:
    def __init__(self, root):
        # Constructor - GUI initialize karte hain jab object create hota hai
        self.root = root  # main window reference store kiya
        self.root.title("Linear Equation Solver — Ax = B")  # window title set kiya
        self.root.geometry("1150x800")  # window size set kiya (width x height)
        self.A_entries = []  # Matrix A ke entries store karne ke liye empty list
        self.B_entries = []  # Matrix B ke entries store karne ke liye empty list
        self._build_ui()  # UI build karo - widgets create karo

    def _build_ui(self):
        # ----- DIMENSIONS SECTION -----
        # User se matrix dimensions input lete hain (rows, columns)
        top = ttk.LabelFrame(self.root, text="Dimensions")  # labeled frame banaya
        top.pack(fill="x", padx=10, pady=6)  # horizontally expand karo, padding add kiya

        ttk.Label(top, text="Rows (A):").grid(row=0, column=0, padx=5, pady=6)  # label place kiya
        self.rows_var = tk.StringVar(value="3")  # String variable - default value "3"
        ttk.Entry(top, textvariable=self.rows_var, width=6).grid(row=0, column=1)  # entry box place kiya

        ttk.Label(top, text="Cols (A) [must equal Rows]:").grid(row=0, column=2, padx=5)  # label place kiya
        self.cols_var = tk.StringVar(value="3")  # String variable - default value "3"
        ttk.Entry(top, textvariable=self.cols_var, width=6).grid(row=0, column=3)  # entry box place kiya

        ttk.Label(top, text="Cols (B):").grid(row=0, column=4, padx=5)  # label place kiya
        self.bcols_var = tk.StringVar(value="1")  # String variable - default value "1"
        ttk.Entry(top, textvariable=self.bcols_var, width=6).grid(row=0, column=5)  # entry box place kiya

        ttk.Button(top, text="Build Grids", command=self.build_grids).grid(row=0, column=6, padx=10)  # button place kiya
        # command=self.build_grids - button click hone par ye function call hoga

        # ----- INPUT FRAMES -----
        # Matrix A aur Matrix B ke input grids - user values yahan fill karega
        mid = ttk.Frame(self.root)  # frame banaya
        mid.pack(fill="both", expand=False, padx=10, pady=6)  # vertically expand nahi karo

        self.A_frame = ttk.LabelFrame(mid, text="Matrix A (coefficients)")  # A matrix ka frame
        self.A_frame.pack(side="left", fill="both", expand=True, padx=5)  # left side place kiya

        self.B_frame = ttk.LabelFrame(mid, text="Matrix B (constants)")  # B matrix ka frame
        self.B_frame.pack(side="left", fill="both", expand=True, padx=5)  # left side place kiya

        # ----- ACTION BUTTONS -----
        # Solve, random fill, clear ke buttons - user actions ke liye
        btns = ttk.Frame(self.root)  # frame banaya
        btns.pack(fill="x", padx=10, pady=4)  # horizontally expand karo

        ttk.Button(btns, text="Solve", command=self.solve).pack(side="left", padx=5)  # solve button
        ttk.Button(btns, text="Random Fill (test)", command=self.random_fill).pack(side="left", padx=5)  # random fill button
        ttk.Button(btns, text="Clear Results", command=self.clear_results).pack(side="left", padx=5)  # clear button

        # ----- RESULTS SECTION -----
        # Solution display area with scrollbar - results yahan dikhte hain
        bottom = ttk.LabelFrame(self.root, text="Results")  # labeled frame banaya
        bottom.pack(fill="both", expand=True, padx=10, pady=6)  # dono directions expand karo

        self.result_text = tk.Text(bottom, wrap="word", font=("Courier", 10))  # text widget banaya
        self.result_text.pack(side="left", fill="both", expand=True, padx=5, pady=5)  # left side place kiya

        scrollbar = ttk.Scrollbar(bottom, command=self.result_text.yview)  # scrollbar banaya
        scrollbar.pack(side="right", fill="y")  # right side place kiya vertically
        self.result_text.configure(yscrollcommand=scrollbar.set)  # scrollbar se text widget connect kiya

    def build_grids(self):
        # ----- PURANE GRIDS DESTROY KARO -----
        # Pehle purane widgets ko destroy karte hain taaki naye grids clean ban jayein
        for w in self.A_frame.winfo_children():  # A frame ke sab children widgets ko loop mein lo
            w.destroy()  # widget destroy karo
        for w in self.B_frame.winfo_children():  # B frame ke sab children widgets ko loop mein lo
            w.destroy()  # widget destroy karo
        self.A_entries, self.B_entries = [], []  # lists clear karo - naye entries store honge

        # ----- DIMENSIONS VALIDATE KARO -----
        # User se dimensions le kar validate karte hain
        try:  # try block - error handle karne ke liye
            r = int(self.rows_var.get())  # rows = StringVariable se integer mein convert karo
            c = int(self.cols_var.get())  # columns = StringVariable se integer mein convert karo
            bc = int(self.bcols_var.get())  # B columns = StringVariable se integer mein convert karo
        except ValueError:  # agar conversion fail ho gaya
            messagebox.showerror("Error", "Dimensions must be integers")  # error popup dikhao
            return  # function se bahar nikal jao

        if r <= 0 or c <= 0 or bc <= 0:  # agar koi dimension 0 ya negative hai
            messagebox.showerror("Error", "Dimensions must be positive")  # error popup dikhao
            return  # function se bahar nikal jao
        if r != c:  # agar rows != cols hai (non-square matrix)
            messagebox.showerror("Error", "Matrix A must be square (rows = cols)")  # error popup dikhao
            return  # function se bahar nikal jao
        if r > 20:  # agar rows 20 se zyada hain (GUI performance issue)
            messagebox.showerror("Error", "Grid too large (max 20 rows for GUI). Use CLI for big matrices.")  # error popup dikhao
            return  # function se bahar nikal jao

        # ----- MATRIX A GRID BANAO -----
        # A matrix ke liye entry boxes create karte hain
        for i in range(r):  # har row ke liye loop - i = row index
            row = []  # temporary row banaya - current row ke entries store karne ke liye
            for j in range(c):  # har column ke liye loop - j = column index
                e = ttk.Entry(self.A_frame, width=9, justify="center")  # entry box banaya (center aligned)
                e.grid(row=i, column=j, padx=2, pady=2)  # grid layout mein place kiya
                e.insert(0, "0")  # default value "0" insert kiya
                row.append(e)  # entry ko row list mein add kiya
            self.A_entries.append(row)  # row ko main A_entries list mein add kiya

        # ----- MATRIX B GRID BANAO -----
        # B matrix ke liye entry boxes create karte hain
        for i in range(r):  # har row ke liye loop - i = row index
            row = []  # temporary row banaya - current row ke entries store karne ke liye
            for j in range(bc):  # har column ke liye loop - j = column index
                e = ttk.Entry(self.B_frame, width=9, justify="center")  # entry box banaya (center aligned)
                e.grid(row=i, column=j, padx=2, pady=2)  # grid layout mein place kiya
                e.insert(0, "0")  # default value "0" insert kiya
                row.append(e)  # entry ko row list mein add kiya
            self.B_entries.append(row)  # row ko main B_entries list mein add kiya

    def random_fill(self):
        # ----- TESTING KE LIYE RANDOM VALUES FILL KARTE HAIN -----
        # Quick testing ke liye sab entries mein random values daal dete hain
        import random  # random module import kiya
        for row in self.A_entries:  # A matrix ke har row ke liye loop
            for e in row:  # row ke har entry ke liye loop
                e.delete(0, tk.END)  # purana value clear karo (index 0 se end tak delete)
                e.insert(0, str(random.uniform(-100.00, 100.00)))  # random value daalo (-100 to 100 range)
        for row in self.B_entries:  # B matrix ke har row ke liye loop
            for e in row:  # row ke har entry ke liye loop
                e.delete(0, tk.END)  # purana value clear karo (index 0 se end tak delete)
                e.insert(0, str(random.uniform(-100.00, 100.00)))  # random value daalo (-100 to 100 range)

    def clear_results(self):
        # ----- RESULTS TEXT BOX CLEAR KARO -----
        # Text widget mein purana text clear karte hain
        self.result_text.delete("1.0", tk.END)  # index "1.0" se end tak delete karo
        # "1.0" = line 1, column 0 (starting position)

    def _read_matrix(self, entries, name):
        # ----- GUI ENTRIES SE MATRIX DATA READ KARTE HAIN -----
        # Entry boxes se values extract karke 2D list mein convert karte hain
        data = []  # main matrix list banaya
        for i, row in enumerate(entries):  # entries list ke har row ke liye loop (i = row index)
            data_row = []  # temporary row banaya - current row ke values store karne ke liye
            for j, e in enumerate(row):  # row ke har entry ke liye loop (j = column index)
                try:  # try block - error handle karne ke liye
                    val = float(e.get())  # entry se string value lo aur float mein convert karo
                except ValueError:  # agar float conversion fail ho gaya
                    raise ValueError(f"{name}[{i+1}][{j+1}] is not a number")  # error raise karo with position
                data_row.append(val)  # value ko current row mein add kiya
            data.append(data_row)  # current row ko main matrix mein add kiya
        return data  # matrix return karo

    def solve(self):
        # ----- COMPLETE GAUSSIAN ELIMINATION SOLVE -----
        # User ke input ko le kar Gaussian elimination process execute karte hain
        self.clear_results()  # pehle results text box clear karo - naye results ke liye
        if not self.A_entries or not self.B_entries:  # agar grids nahi build kiye
            messagebox.showerror("Error", "Click 'Build Grids' first")  # error popup dikhao
            return  # function se bahar nikal jao

        # ----- MATRICES READ KARO -----
        # GUI entries se values extract karke Python lists mein convert karte hain
        try:  # try block - error handle karne ke liye
            A = self._read_matrix(self.A_entries, "A")  # A matrix read karo
            B = self._read_matrix(self.B_entries, "B")  # B matrix read karo
        except ValueError as e:  # agar read mein error aaya
            messagebox.showerror("Input Error", str(e))  # error popup dikhao
            return  # function se bahar nikal jao

        # ----- SOLVE KARO -----
        # Gaussian elimination ke steps execute karte hain
        try:  # try block - error handle karne ke liye
            r = len(A)  # rows count nikala
            bc = len(B[0])  # B columns count nikala
            A_orig = [row[:] for row in A]  # original A ka copy banaya (error check ke liye)
            B_orig = [row[:] for row in B]  # original B ka copy banaya (error check ke liye)

            AUG = [A[i] + B[i] for i in range(r)]  # augmented matrix banao (A + B combine)
            total_cols = len(AUG[0])  # total columns count nikala

            self._log("=" * 64)  # separator line log kiya
            self._log(f"System: Ax = B   |  A: {r}x{r}   |  B: {r}x{bc}")  # system info log kiya
            self._log("=" * 64)  # separator line log kiya
            self._log("\nAugmented matrix [A | B]:")  # header log kiya
            self._print_matrix(AUG, r, r)  # augmented matrix print kiya

            AUG = self._eliminate(AUG, r, total_cols)  # forward elimination - upper triangular form
            self._log("\n" + "-" * 64)  # separator line log kiya
            self._log("Upper triangular form after elimination:")  # header log kiya
            self._print_matrix(AUG, r, r)  # upper triangular matrix print kiya

            X = self._back_sub(AUG, r, bc)  # back substitution - solution nikalo
            self._log("\n" + "=" * 64)  # separator line log kiya
            self._log("FINAL SOLUTION:")  # header log kiya
            self._log("=" * 64)  # separator line log kiya
            for i in range(r):  # har row ke liye loop
                parts = [f"X[{i}][{j}] = {X[i][j]:.6f}" for j in range(bc)]  # format solution string
                self._log("  " + "   ".join(parts))  # solution log kiya

            max_err = self._residual(A_orig, X, B_orig)  # error check - residual calculate karo
            self._log("\n" + "-" * 64)  # separator line log kiya
            self._log(f"Max residual  ||Ax - b||_inf = {max_err:.3e}")  # error log kiya
            self._log("=" * 64)  # separator line log kiya

        except ValueError as e:  # agar solve mein error aaya
            messagebox.showerror("Solve Error", str(e))  # error popup dikhao
            self._log(f"\nERROR: {e}")  # error log kiya
        except Exception as e:  # agar unexpected error aaya
            messagebox.showerror("Unexpected Error", str(e))  # error popup dikhao

    def _eliminate(self, AUG, r, total_cols):
        # ----- FORWARD ELIMINATION WITH PARTIAL PIVOTING -----
        # Upper triangular form banate hain - diagonal ke neeche sab elements zero
        max_val = max(abs(AUG[i][j]) for i in range(r) for j in range(r))  # matrix mein sabse bada element dhundho
        TOL = 1e-12 * max(max_val, 1.0)  # tolerance set kiya (singular check ke liye)
        for i in range(r):  # har row ke liye loop - i = current row index
            # ----- PARTIAL PIVOTING -----
            # Current column mein sabse bada element dhundho (pivot)
            pivot_row, pivot_val = i, abs(AUG[i][i])  # initially current row hi pivot hai
            for k in range(i + 1, r):  # rows below current row check karo
                if abs(AUG[k][i]) > pivot_val:  # agar k-th row mein bada element mila
                    pivot_val, pivot_row = abs(AUG[k][i]), k  # pivot value aur row update karo
            if pivot_val < TOL:  # singular check - agar pivot bahut chhota hai
                raise ValueError(f"Matrix is singular (column {i+1})")  # error raise karo
            if pivot_row != i:  # agar pivot row change hua
                AUG[i], AUG[pivot_row] = AUG[pivot_row], AUG[i]  # rows swap kar do
                self._log(f"  [swap] row {i+1} <-> row {pivot_row+1}")  # swap log kiya
            diag = AUG[i][i]  # diagonal element (pivot) store kiya
            # ----- ELIMINATION -----
            # Rows below current row ko eliminate karte hain
            for h in range(i + 1, r):  # H = row index (current row ke neeche)
                factor = AUG[h][i] / diag  # elimination factor calculate karo
                # Factor = h-th row mein i-th column ko zero banane ke liye multiplier
                for j in range(total_cols):  # har column ke liye loop
                    AUG[h][j] -= factor * AUG[i][j]  # eliminate karo (in-place subtraction)
                    # Formula: new_value = old_value - factor * pivot_row_value
        return AUG  # upper triangular matrix return karo

    def _back_sub(self, AUG, r, bc):
        # ----- BACK SUBSTITUTION -----
        # Upper triangular matrix se solution nikalte hain
        X = [[0.0] * bc for _ in range(r)]  # solution matrix banaya - sabse pehle zeros
        max_val = max(abs(AUG[i][i]) for i in range(r))  # diagonal mein sabse bada element dhundho
        TOL = 1e-12 * max(max_val, 1.0)  # tolerance set kiya (singular check ke liye)
        for b_col in range(bc):  # har B column ke liye loop (multiple RHS support)
            rhs_col = r + b_col  # RHS column ka index calculate kiya
            for i in reversed(range(r)):  # ulta loop - last row se first row tak
                # reversed(range(n)) = [n-1, n-2, ..., 0]
                s = AUG[i][rhs_col]  # RHS value lo - augmented matrix ke last column se
                for j in range(i + 1, r):  # pehle se solve kiye variables ke terms
                    # Diagonal ke right side wale columns - jo already solve ho chuke hain
                    s -= AUG[i][j] * X[j][b_col]  # known terms ko equation se hatao
                    # Formula: new_RHS = old_RHS - coefficient * known_value
                if abs(AUG[i][i]) < TOL:  # singular check - agar zero ke bahut qareeb hai
                    raise ValueError(f"Singular at row {i+1}")  # error raise karo
                X[i][b_col] = s / AUG[i][i]  # divide karo variable isolate karne ke liye
                # Formula: variable = RHS / diagonal_coefficient
        return X  # solution matrix return karo

    def _residual(self, A, X, B):
        # ----- RESIDUAL ERROR CALCULATE KARO (AX - B) -----
        # Solution verify karte hain - AX calculate karke B se compare karte hain
        max_err = 0.0  # maximum error store karne ke liye - initially 0
        for i in range(len(A)):  # har row ke liye loop - i = row index of A
            for j in range(len(X[0])):  # har column ke liye loop - j = column index of X
                calc = sum(A[i][k] * X[k][j] for k in range(len(X)))  # A*X calculate karo
                # Formula: (A*X)[i][j] = sum(A[i][k] * X[k][j]) for all k
                max_err = max(max_err, abs(calc - B[i][j]))  # error update karo
                # Error = |calculated - actual| - absolute value
        return max_err  # maximum error return karo

    def _print_matrix(self, M, rows, split_col):
        # ----- MATRIX KO CLEAN FORMAT MEIN PRINT KARO -----
        # Matrix ko visual format mein log karte hain with | separator
        for i, row in enumerate(M):  # har row ke liye loop (i = row index)
            left = "  ".join(f"{v:9.3f}" for v in row[:split_col])  # A part (left side)
            # row[:split_col] = first split_col elements (A matrix)
            # f"{v:9.3f}" = 9 characters wide, 3 decimal places
            right = "  ".join(f"{v:9.3f}" for v in row[split_col:])  # B part (right side)
            # row[split_col:] = remaining elements (B matrix)
            self._log(f"  [ {left}  |  {right} ]")  # formatted row log kiya

    def _log(self, text):
        # ----- TEXT KO RESULTS BOX MEIN ADD KARO -----
        # Log function - text widget mein text add karte hain
        self.result_text.insert(tk.END, text + "\n")  # text insert kiya end pe with newline
        self.result_text.see(tk.END)  # scroll to end - naya text dikhane ke liye


if __name__ == "__main__":
    # ----- MAIN ENTRY POINT -----
    # Python script directly run hone par ye code execute hota hai
    root = tk.Tk()  # main window create karo (root window)
    try:  # try block - theme set karne ke liye
        ttk.Style().theme_use("clam")  # clean theme set karo (better appearance)
    except Exception:  # agar theme fail ho gaya
        pass  # ignore karo - default theme use hoga
    app = LinearSolverGUI(root)  # app instance create karo - GUI initialize hota hai
    root.mainloop()  # event loop start karo - window open hota hai