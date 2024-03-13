# # def main():
# #     M = 32768
# #     mid = []
# #     s, e = -M, M + 1
# #     s_flag = e_flag = False
# #     for line in open(0):
# #         tmp = line.rstrip().replace("||", "").split("&&")
# #         n = len(tmp)
# #         if n == 1:
# #             if "<" in (t := tmp[0]):
# #                 s = max(s, int(t.split("= ")[1]))
# #                 s_flag = True
# #             else:
# #                 e = min(e, int(t.split("= ")[1]))
# #                 e_flag = True
# #         else:
# #             a, b = int(tmp[0].split("= ")[1]), int(tmp[1].split("= ")[1])
# #             if a <= b:
# #                 mid.append([a, b + 1])

# #     if s + 1 >= e:
# #         print("true")
# #         return
# #     if s_flag:
# #         mid.append([-M + 1, min(s, M) + 1])
# #     if e_flag:
# #         mid.append([max(e, -M + 1), M + 1])

# #     n_mid = []
# #     if mid:
# #         m = len(mid)
# #         mid.sort()
# #         a0, b0 = mid[0]
# #         _, b1 = mid[-1]

# #         if m < 2:
# #             n_mid = [[mid[0][0], mid[0][1] - 1]]

# #         for a1, b1 in mid[1:]:
# #             if a1 <= b0:
# #                 b0 = max(b0, b1)
# #                 continue
# #             else:
# #                 n_mid.append((a0, b0 - 1))
# #                 a0, b0 = a1, b1
# #         n_mid.append((a0, b0 - 1))

# #         if n_mid and n_mid[0][0] == -m and n_mid[0][1] == m:
# #             print("true")
# #             return

# #     ans = []
# #     if n_mid:
# #         ans = [f"x >= {a} && x <= {b}" for a, b in n_mid]
# #     if ans:
# #         ans[0] = ans[0].replace(f"x >= -{M-1} && ", "")
# #         ans[-1] = ans[-1].replace(f" && x <= {M}", "")

# #     print(" ||\n".join(ans) or "false")


# # main()


# def main():
#     M = 32768
#     ans = set()
#     s, e = -M - 1, M
#     s_flag = e_flag = False
#     for line in open(0):
#         tmp = line.rstrip().replace(" ||", "").split(" &&")
#         n = len(tmp)
#         if n == 1:
#             if "<" in (t := tmp[0]):
#                 s = max(s, int(t.split("= ")[1]))
#                 s_flag = True
#             else:
#                 e = min(e, int(t.split("= ")[1]))
#                 e_flag = True
#         else:
#             a, b = int(tmp[0].split("= ")[1]), int(tmp[1].split("= ")[1])
#             if a <= b:
#                 ans |= set(range(a, b + 1))
#     if s_flag:
#         ans |= set(range(-M, s + 1))
#     if e_flag:
#         ans |= set(range(e, M))

#     if m := len(ans):
#         if m == M * 2:
#             print("true")
#         else:
#             tmp = []
#             ans = sorted(ans)
#             a = b = ans[0]
#             for c in ans[1:]:
#                 if b + 1 == c:
#                     b = c
#                     continue
#                 tmp.append(f"x >= {a} && x <= {b}")
#                 a = b = c
#             tmp.append(f"x >= {a} && x <= {b}")
#             if tmp[0] != f"x >= {-M} && x <= {-M}":
#                 tmp[0] = tmp[0].replace(f"x >= {-M} && ", "")
#             if tmp[-1] != f"x >= {M-1} && x <= {M-1}":
#                 tmp[-1] = tmp[-1].replace(f" && x <= {M-1}", "")
#             print(" ||\n".join(tmp))
#     else:
#         print("false")


# main()


def main():
    inf = 32768
    low = -inf
    high = inf
    low_flag = high_flag = False
    expressions = []

    for line in open(0):
        line = line.strip().replace("||", "").split("&&")
        n = len(line)

        if n == 1:
            if "<" in line[0]:
                low = max(low, int(line[0].split("= ")[1]))
                low_flag = True
            else:
                high = min(high, int(line[0].split("= ")[1]))
                high_flag = True
        else:
            a, b = int(line[0].split("= ")[1]), int(line[1].split("= ")[1])
            if a <= b:
                expressions.append((a, b))

    if low_flag:
        expressions.append((-inf, low))
    if high_flag:
        expressions.append((high, inf - 1))

    ans = set()
    for a, b in expressions:
        ans |= set(range(a, b + 1))

    if ans:
        if len(ans) == 2 * inf:
            print("true")
        else:
            tmp = []
            ans = sorted(ans)
            a = b = ans[0]
            for c in ans[1:]:
                if b + 1 == c:
                    b = c
                    continue
                tmp.append(f"x >= {a} && x <= {b}")
                a = b = c
            tmp.append(f"x >= {a} && x <= {b}")
            if tmp[0] != f"x >= {-inf} && x <= {-inf}":
                tmp[0] = tmp[0].replace(f"x >= {-inf} && ", "")
            if tmp[-1] != f"x >= {inf-1} && x <= {inf-1}":
                tmp[-1] = tmp[-1].replace(f" && x <= {inf-1}", "")
            print(" ||\n".join(tmp))
    else:
        print("false")


main()
