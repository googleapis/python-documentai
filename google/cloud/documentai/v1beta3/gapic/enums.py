# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wrappers for protocol buffer enum types."""

import enum


class BatchProcessMetadata(object):
    class State(enum.IntEnum):
        """
        Possible states of the batch processing operation.

        Attributes:
          STATE_UNSPECIFIED (int): The default value. This value is used if the state is omitted.
          WAITING (int): Request operation is waiting for scheduling.
          RUNNING (int): Request is being processed.
          SUCCEEDED (int): The batch processing completed successfully.
          CANCELLING (int): The batch processing was being cancelled.
          CANCELLED (int): The batch processing was cancelled.
          FAILED (int): The batch processing has failed.
        """

        STATE_UNSPECIFIED = 0
        WAITING = 1
        RUNNING = 2
        SUCCEEDED = 3
        CANCELLING = 4
        CANCELLED = 5
        FAILED = 6


class Document(object):
    class Page(object):
        class Layout(object):
            class Orientation(enum.IntEnum):
                """
                Detected human reading orientation.

                Attributes:
                  ORIENTATION_UNSPECIFIED (int): Unspecified orientation.
                  PAGE_UP (int): Orientation is aligned with page up.
                  PAGE_RIGHT (int): Orientation is aligned with page right.
                  Turn the head 90 degrees clockwise from upright to read.
                  PAGE_DOWN (int): Orientation is aligned with page down.
                  Turn the head 180 degrees from upright to read.
                  PAGE_LEFT (int): Orientation is aligned with page left.
                  Turn the head 90 degrees counterclockwise from upright to read.
                """

                ORIENTATION_UNSPECIFIED = 0
                PAGE_UP = 1
                PAGE_RIGHT = 2
                PAGE_DOWN = 3
                PAGE_LEFT = 4

        class Token(object):
            class DetectedBreak(object):
                class Type(enum.IntEnum):
                    """
                    Enum to denote the type of break found.

                    Attributes:
                      TYPE_UNSPECIFIED (int): Unspecified break type.
                      SPACE (int): A single whitespace.
                      WIDE_SPACE (int): A wider whitespace.
                      HYPHEN (int): A hyphen that indicates that a token has been split across lines.
                    """

                    TYPE_UNSPECIFIED = 0
                    SPACE = 1
                    WIDE_SPACE = 2
                    HYPHEN = 3

    class PageAnchor(object):
        class PageRef(object):
            class LayoutType(enum.IntEnum):
                """
                The type of layout that is being referenced.

                Attributes:
                  LAYOUT_TYPE_UNSPECIFIED (int): Layout Unspecified.
                  BLOCK (int): References a ``Page.blocks`` element.
                  PARAGRAPH (int): References a ``Page.paragraphs`` element.
                  LINE (int): References a ``Page.lines`` element.
                  TOKEN (int): References a ``Page.tokens`` element.
                  VISUAL_ELEMENT (int): References a ``Page.visual_elements`` element.
                  TABLE (int): Refrrences a ``Page.tables`` element.
                  FORM_FIELD (int): References a ``Page.form_fields`` element.
                """

                LAYOUT_TYPE_UNSPECIFIED = 0
                BLOCK = 1
                PARAGRAPH = 2
                LINE = 3
                TOKEN = 4
                VISUAL_ELEMENT = 5
                TABLE = 6
                FORM_FIELD = 7

    class Provenance(object):
        class OperationType(enum.IntEnum):
            """
            If a processor or agent does an explicit operation on existing elements.

            Attributes:
              OPERATION_TYPE_UNSPECIFIED (int): Operation type unspecified.
              ADD (int): Add an element. Implicit if no ``parents`` are set for the
              provenance.
              REMOVE (int): The element is removed. No ``parents`` should be set.
              REPLACE (int): Explicitly replaces the element(s) identified by ``parents``.
              EVAL_REQUESTED (int): Element is requested for human review.
              EVAL_APPROVED (int): Element is review and approved at human review, confidence will be set
              to 1.0
            """

            OPERATION_TYPE_UNSPECIFIED = 0
            ADD = 1
            REMOVE = 2
            REPLACE = 3
            EVAL_REQUESTED = 4
            EVAL_APPROVED = 5


class ReviewDocumentOperationMetadata(object):
    class State(enum.IntEnum):
        """
        State of the longrunning operation.

        Attributes:
          STATE_UNSPECIFIED (int): Unspecified state.
          RUNNING (int): Operation is still running.
          CANCELLING (int): Operation is being cancelled.
          SUCCEEDED (int): Operation succeeded.
          FAILED (int): Operation failed.
          CANCELLED (int): Operation is cancelled.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        CANCELLING = 2
        SUCCEEDED = 3
        FAILED = 4
        CANCELLED = 5
