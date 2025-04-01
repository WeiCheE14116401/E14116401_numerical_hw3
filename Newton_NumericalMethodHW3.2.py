# 給定的數據點 (y_i, x_i)
y_data = [0.740818, 0.670320, 0.606531, 0.548812]  # y 值
x_data = [0.3, 0.4, 0.5, 0.6]                      # x 值

# 計算牛頓插值的差商表
def compute_divided_differences(y_data, x_data):
    n = len(y_data)
    # 初始化差商表
    f = [[0.0] * n for _ in range(n)]
    
    # 零階差商
    for i in range(n):
        f[i][0] = x_data[i]
    
    # 計算差商
    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i + 1][j - 1] - f[i][j - 1]) / (y_data[i + j] - y_data[i])
    
    return f

# 使用牛頓插值計算 P(y)
def newton_interpolation(y_data, x_data, y_val):
    n = len(y_data)
    f = compute_divided_differences(y_data, x_data)
    
    # 牛頓插值公式
    result = f[0][0]  # 零階差商
    term = 1.0
    for i in range(1, n):
        term *= (y_val - y_data[i - 1])
        result += f[0][i] * term
    return result


def main():

    y_val = float(input("請輸入 y 值："))
    
    p_y = newton_interpolation(y_data, x_data, y_val)
    
    print(f"P({y_val}) = {p_y:.6f}")
    
    diff = abs(y_val - p_y)

if __name__ == "__main__":
    main()