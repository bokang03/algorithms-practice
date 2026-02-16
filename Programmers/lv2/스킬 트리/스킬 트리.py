def solution(skill, skill_trees):
    succes = 0

    for skill_tree in skill_trees:
        result = True
        n = -1
        for s in skill:
            if s not in skill_tree:  # 스킬이 없다면 다음 스킬 나오면 False걸리게 27
                n = 27
            elif skill_tree.index(s) < n:  # 검증 스킬이 이전 스킬보다 뒤에 나오면 False
                result = False
                break
            else:
                n = skill_tree.index(s)

        if result == True:
            succes += 1
    return succes