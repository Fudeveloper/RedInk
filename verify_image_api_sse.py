#!/usr/bin/env python3
"""
验证 ImageApiGenerator SSE 功能实现
"""

import os
import re

def check_image_api_generator():
    """检查 ImageApiGenerator 实现"""
    print("=" * 60)
    print("检查 ImageApiGenerator 实现")
    print("=" * 60)

    image_api_file = os.path.join('backend', 'generators', 'image_api.py')

    if not os.path.exists(image_api_file):
        print(f"❌ 文件不存在: {image_api_file}")
        return False

    try:
        with open(image_api_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查SSE配置读取
        if 'self.use_sse = config.get(\'use_sse\', False)' in content:
            print("✅ 包含 SSE 配置读取")
        else:
            print("❌ 缺少 SSE 配置读取")
            return False

        # 检查SSE流式方法
        if 'def generate_image_stream(' in content:
            print("✅ 包含 SSE 流式生成方法")
        else:
            print("❌ 缺少 SSE 流式生成方法")
            return False

        # 检查images API流式方法
        if 'def _generate_via_images_api_stream(' in content:
            print("✅ 包含 images API 流式方法")
        else:
            print("❌ 缺少 images API 流式方法")
            return False

        # 检查chat API流式方法
        if 'def _generate_via_chat_api_stream(' in content:
            print("✅ 包含 chat API 流式方法")
        else:
            print("❌ 缺少 chat API 流式方法")
            return False

        # 检查stream=True配置
        if '"stream": True' in content:
            print("✅ 包含 stream=True 配置")
        else:
            print("❌ 缺少 stream=True 配置")
            return False

        # 检查Accept: text/event-stream
        if '"Accept": "text/event-stream"' in content:
            print("✅ 包含 SSE 请求头配置")
        else:
            print("❌ 缺少 SSE 请求头配置")
            return False

        return True

    except Exception as e:
        print(f"❌ 检查失败: {str(e)}")
        return False

def check_image_service():
    """检查图片服务中ImageApiGenerator的调用"""
    print("\n" + "=" * 60)
    print("检查图片服务中的 ImageApiGenerator 调用")
    print("=" * 60)

    image_service_file = os.path.join('backend', 'services', 'image.py')

    if not os.path.exists(image_service_file):
        print(f"❌ 文件不存在: {image_service_file}")
        return False

    try:
        with open(image_service_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查image_api的SSE调用
        if "elif self.provider_config.get('type') == 'image_api':" in content:
            print("✅ 包含 image_api 类型处理")
        else:
            print("❌ 缺少 image_api 类型处理")
            return False

        # 检查SSE调用选择
        if "if self.provider_config.get('use_sse', False):" in content:
            print("✅ 包含 image_api SSE 调用选择")
        else:
            print("❌ 缺少 image_api SSE 调用选择")
            return False

        # 检查generate_image_stream调用
        if "for event in self.generator.generate_image_stream(" in content:
            print("✅ 包含 image_api generate_image_stream 调用")
        else:
            print("❌ 缺少 image_api generate_image_stream 调用")
            return False

        # 检查完成事件处理
        if "if event['event'] == 'complete' and 'image_data' in event['data']:" in content:
            print("✅ 包含 image_api 完成事件处理")
        else:
            print("❌ 缺少 image_api 完成事件处理")
            return False

        return True

    except Exception as e:
        print(f"❌ 检查失败: {str(e)}")
        return False

def check_config_validation():
    """检查配置验证中的image_api SSE支持"""
    print("\n" + "=" * 60)
    print("检查配置验证中的 image_api SSE 支持")
    print("=" * 60)

    config_file = os.path.join('backend', 'config.py')

    if not os.path.exists(config_file):
        print(f"❌ 文件不存在: {config_file}")
        return False

    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查image_api类型包含在验证中
        if "if provider_type in ['openai', 'openai_compatible', 'image_api']:" in content:
            print("✅ image_api 包含在类型验证中")
        else:
            print("❌ image_api 不在类型验证中")
            return False

        # 检查SSE配置日志
        if 'use_sse = provider_config.get(\'use_sse\', False)' in content:
            print("✅ 包含 SSE 配置日志")
        else:
            print("❌ 缺少 SSE 配置日志")
            return False

        # 检查SSE状态日志
        if 'logger.info(f"服务商 [{provider_name}] 启用 SSE 流式调用 (type={provider_type})")' in content:
            print("✅ 包含 SSE 启用日志")
        else:
            print("❌ 缺少 SSE 启用日志")
            return False

        return True

    except Exception as e:
        print(f"❌ 检查失败: {str(e)}")
        return False

def check_frontend_implementation():
    """检查前端实现"""
    print("\n" + "=" * 60)
    print("检查前端实现")
    print("=" * 60)

    # 检查ProviderModal
    provider_modal_file = os.path.join('frontend', 'src', 'components', 'settings', 'ProviderModal.vue')

    if os.path.exists(provider_modal_file):
        try:
            with open(provider_modal_file, 'r', encoding='utf-8') as f:
                content = f.read()

                # 检查SSE选项显示
                if "props.formData.type === 'image_api'" in content:
                    print("✅ ProviderModal 支持 image_api 的 SSE 选项")
                else:
                    print("❌ ProviderModal 不支持 image_api 的 SSE 选项")
                    return False

                # 检查SSE选项描述
                if "启用后将以 Server-Sent Events 方式调用图片生成 API" in content:
                    print("✅ ProviderModal 包含 image_api SSE 选项描述")
                else:
                    print("❌ ProviderModal 缺少 image_api SSE 选项描述")
                    return False

        except Exception as e:
            print(f"❌ ProviderModal 检查失败: {str(e)}")
            return False
    else:
        print(f"❌ ProviderModal 文件不存在")
        return False

    # 检查useProviderForm
    provider_form_file = os.path.join('frontend', 'src', 'composables', 'useProviderForm.ts')

    if os.path.exists(provider_form_file):
        try:
            with open(provider_form_file, 'r', encoding='utf-8') as f:
                content = f.read()

                # 检查SSE字段
                if 'use_sse?: boolean' in content and 'ImageProviderForm' in content:
                    print("✅ useProviderForm 包含 image_api SSE 字段")
                else:
                    print("❌ useProviderForm 缺少 image_api SSE 字段")
                    return False

                # 检查SSE保存逻辑
                if 'providerData.use_sse = imageForm.value.use_sse' in content:
                    print("✅ useProviderForm 包含 image_api SSE 保存逻辑")
                else:
                    print("❌ useProviderForm 缺少 image_api SSE 保存逻辑")
                    return False

        except Exception as e:
            print(f"❌ useProviderForm 检查失败: {str(e)}")
            return False
    else:
        print(f"❌ useProviderForm 文件不存在")
        return False

    return True

def check_docker_config():
    """检查Docker配置"""
    print("\n" + "=" * 60)
    print("检查 Docker 配置")
    print("=" * 60)

    docker_config_file = os.path.join('docker', 'image_providers.yaml')

    if not os.path.exists(docker_config_file):
        print(f"❌ Docker 配置文件不存在")
        return False

    try:
        with open(docker_config_file, 'r', encoding='utf-8') as f:
            content = f.read()

            # 检查SSE配置说明
            if 'use_sse: false  # 是否使用SSE流式调用' in content:
                print("✅ Docker 配置包含 SSE 选项说明")
            else:
                print("❌ Docker 配置缺少 SSE 选项说明")
                return False

            return True

    except Exception as e:
        print(f"❌ Docker 配置检查失败: {str(e)}")
        return False

def main():
    """主验证函数"""
    print("开始验证 ImageApiGenerator SSE 功能实现")

    tests = [
        ("ImageApiGenerator 实现", check_image_api_generator),
        ("图片服务调用", check_image_service),
        ("配置验证", check_config_validation),
        ("前端实现", check_frontend_implementation),
        ("Docker 配置", check_docker_config)
    ]

    results = []

    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} 验证异常: {str(e)}")
            results.append((test_name, False))

    # 输出验证结果汇总
    print("\n" + "=" * 60)
    print("验证结果汇总")
    print("=" * 60)

    passed = 0
    total = len(results)

    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{test_name:<20} {status}")
        if result:
            passed += 1

    print(f"\n总计: {passed}/{total} 项验证通过")

    if passed == total:
        print("🎉 所有验证通过！ImageApiGenerator SSE 功能实现完成。")
        return True
    else:
        print("⚠️  部分验证失败，请检查相关实现。")
        return False

if __name__ == "__main__":
    main()