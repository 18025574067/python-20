"""
1、导入模块
2、通过match方法，验证正则
3、判断是否验证成功
4、如果成功，获取匹配的结果

"""
import re

# 1、导入模块

# 2、通过match方法，验证正则
# result = re.match("hello", "xhello@163.com")
# result = re.search("hello", "xhello@163.com")
# match 和 search 的区别
# 1）match 从需要检测的.group的字符串的开头位置匹配，如果失败返回 None
# 2）search 从需要检测的字符串中搜索满足正则的结果，如果成功则返回 match.object 对象

# 一、search 的使用
# result = re.search("\d+", "阅读次数为：9999")

# 二、findall("正则表达式", "待查找的内容") 搜索全部，返回值是列表
# result = re.findall("\d+", "阅读次数为：9999, 转发次数为: 6666, 评论次数为: 38")

# 三、sub("正则表达式", "新的内容", "要替换的字符串") 字符串替换（按照正则，查找字符串并替换为指定的内容）
# 返回值是替换后的字符串
# result = re.sub("\d+", "10000", "阅读次数为：9999, 转发次数为: 6666, 评论次数为: 38")
str1 = """<div class="jobxq"><div class="jobwz"><p style="font-weight: bold; font-size: 16px;"><br></p>

                <p><b><span>运营管理：</span></b></p><p><span>
                1. </span><div class="jobn">店长/卖场经理</div><span>负责门店经营管理事务，根据总部和区域的经营策略，规则，实施方案及制度，制定门店运营计划，</span><span><span></span></span><span>完成公司下达的各项年度计划及运营指标，并不断满足顾客需求，提高门店的核心竞争力；定期向上级管理层汇报店内各项经营业绩、指标完成进度等门店运营情况。</span></p><p><span>
                2.</span><span>负责门店关键业绩指标的达成，包括销售额、</span><span> </span><span>毛利、</span><span> </span><span>营运成本、商品损耗、</span><span> </span><span>利润、库存等；</span></p><p><span>
                3. </span><span>分析当地市场竞争状况、商品和门店潜力，制作门店的商业计划</span></p><p><span>
                4. </span><span>提高门店的销售量和竞争力  </span></p><p><span>
                5.</span><span>定期对营业状态做出总结和分析，并使该结果服务于运营活动中，降低和控制各种损耗 </span></p>
                
                <p><b><span>日常工作管理：</span></b></p><p><span>
                1 .</span><span>确保门店各项业务操作、形象、</span><span></span><span>服务、商品、资金、</span><span> </span><span>资产、安全等符合企业标准</span></p><p><span>
                2 .</span><span>通过检查与生产流程，保障食品卫生与质量，维护公司资产，确保环境，产品，顾客，员工，设备的安全 </span></p><p><span>
                3.</span><span>对门店组织结构进行优化高效管理；在门店日常管理和新项目的实施中体现创新精神</span></p><p><span>
                4.</span><span>高效执行商品政策（商品组合，陈列，价格，品质，信息及物流）；确保团队遵守相应法规（商品法，劳动法，食品卫生，环境等） </span></p><p><span>
                5</span><span>、及时协调处理各类紧急、突发事件，以及门店的安全及顾客投诉等工作</span></p><p><span>
                6. .</span><span>监控门店的各项成本收支；确保店内资金的安全流转 </span></p><p><span>
                7.</span><span>通过内部沟通和培训及晋升机制为公司发展积极培育人才，制定阶段性的发展目标和实施计划，持续提升团队的销售业绩和人员素质，激励团队构建良好员工关系，鼓励个人发展和达到团队成功 </span></p><p><span>
                8.</span><span>计划并实施对直接下属的目标管理，检查、督导各级管理者的工作，协调店内各部门之间的关系，评估、考核直接下属</span></p><p>  </p>
                
                <p><b><span>职位要求：</span></b></p>
                <p><span>1.</span><span>大专以上学历 </span></p>
                <p><span>2. </span><span>五年以上零售行业管理工作经验</span><span>,</span><span>三年以上大型零售行业店长经验</span></p>
                <p><span>3. </span><span>良好的沟通和人际交往技巧</span></p><p><span><span></span></span><span>良好的逻辑分析和判断能力，优秀的执行能力</span></p><p><span><span></span></span><span>良好的演讲技巧和谈判能力 </span></p>
                 <p><span>4.</span><span>商品意识及市场判断能力强，丰富的商品知识，精通超市运转流程</span>
                 <span><br>5.</span><span>高度的商业敏锐度，能准确把握大型门店销售及价格运作，对商品、营销和业绩提升等有较强的操控技能 </span></p>
                 <p><span>6. </span><span>具备电脑操作知识，英语熟练者优先</span></p>
                 <p style="font-weight: bold; font-size: 16px;"><br></p></div>
                
                <div class="btns"><div class="apply">立即申请</div>
                
                <div class="back">返回职位列表</div></div></div>

"""
# result = re.sub("<[^>]+>| |\n", "", str1)

# 四、split("正则表达式", "待拆分的字符串")，按照正则去拆分字符串，返回结果是列表
result = re.split(" |:", "info:hello@163.com zhangsan lisi")

# 3、判断是否验证成功
if result:
    print("匹配成功！")

    # 4、如果成功，获取匹配的结果
    # print("匹配结果：", result.group())
    print("匹配结果：", result)
else:
    print("匹配失败！")
