# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making
蓝鲸智云 - PaaS 平台 (BlueKing - PaaS System) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except
in compliance with the License. You may obtain a copy of the License at

    http://opensource.org/licenses/MIT

Unless required by applicable law or agreed to in writing, software distributed under
the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the specific language governing permissions and
limitations under the License.

We undertake not to change the open source license (MIT license) applicable
to the current version of the project delivered to anyone in the future.
"""
# Generated by Django 3.2.12 on 2023-04-17 03:13

from django.db import migrations
import jsonfield.fields
import paasng.engine.models.deployment


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0012_auto_20220510_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployment',
            name='processes',
            field=paasng.engine.models.deployment.DeclarativeProcessField(default=dict, help_text='进程定义，在准备阶段 PaaS 会从源码(或配置)读取应用的启动进程, 并更新该字段。在发布阶段会从该字段读取 procfile 和同步 ProcessSpec'),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='procfile',
            field=jsonfield.fields.JSONField(default=dict, help_text='[deprecated] 启动命令, 在准备阶段 PaaS 会从源码(或配置)读取应用的 procfile, 并更新该字段, 在发布阶段将从该字段读取 procfile'),
        ),
    ]