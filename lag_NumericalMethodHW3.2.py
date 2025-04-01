# 拉格朗日插值法計算機

# 給定的數據點 (y_i, x_i)
y_data = [0.740818, 0.670320, 0.606531, 0.548812]  # y 值
x_data = [0.3, 0.4, 0.5, 0.6]                      # x 值

# 計算拉格朗日插值多項式 P(y)
def lagrange_interpolation(y_data, x_data, y_val):
    n = len(y_data)
    result = 0.0

    # 計算 P(y) = sum(x_i * L_i(y))
    for i in range(n):
        term = x_data[i]  # 從 x_i 開始
        for j in range(n):
            if j != i:
                term *= (y_val - y_data[j]) / (y_data[i] - y_data[j])
        result += term
    
    return result

# 主程式
def main():

    y_val = float(input("請輸入 y 值："))
    
    p_y = lagrange_interpolation(y_data, x_data, y_val)
    
    # 輸出結果
    print(f"P({y_val}) = {p_y:.6f}")
    
    # 檢查 |y - P(y)| 是否小於 10^-4
    diff = abs(y_val - p_y)
    if diff < 1e-4:
        print(f"提示：輸入值 y = {y_val:.6f} 與輸出值 P(y) = {p_y:.6f} 的差值 {diff:.6f} 小於 10^-4")

if __name__ == "__main__":
    main()